import React from 'react';

export function CandidateKanban({ candidate }: { candidate: any }) {
  if (!candidate) return null;

  return (
    <div style={{ marginTop: '1.5rem', padding: '1.5rem', background: '#f8fafc', border: '1px solid #e2e8f0', borderRadius: '8px' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <h4 style={{ margin: 0, color: '#0f172a' }}>Candidate Match Score: {candidate.matchScore}%</h4>
        <span style={{ padding: '0.25rem 0.75rem', background: candidate.status === 'RECOMMENDED' ? '#059669' : '#d97706', color: '#fff', borderRadius: '12px', fontSize: '12px', fontWeight: 'bold' }}>
          {candidate.status}
        </span>
      </div>
      <p style={{ color: '#475569', marginTop: '0.5rem' }}><strong>Matched Target Skills:</strong> {candidate.matchedSkills.join(', ')}</p>

      <div style={{ marginTop: '1rem', borderTop: '1px solid #cbd5e1', paddingTop: '0.75rem' }}>
        <strong style={{ fontSize: '12px', color: '#475569' }}>Synthesized Technical Interview Questions:</strong>
        <ol style={{ margin: '0.5rem 0 0 1.25rem', color: '#334155', fontSize: '13px' }}>
          {candidate.generatedQuestions.map((q: string, i: number) => (
            <li key={i}>{q}</li>
          ))}
        </ol>
      </div>
    </div>
  );
}
