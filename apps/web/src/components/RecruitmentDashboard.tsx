import React from 'react';

export function RecruitmentDashboard({ total }: { total: number }) {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: '1rem', marginBottom: '1.5rem' }}>
      <div style={{ background: '#fff', padding: '1.25rem', borderRadius: '8px', border: '1px solid #e2e8f0' }}>
        <div style={{ fontSize: '12px', color: '#64748b', fontWeight: 'bold' }}>TOTAL CANDIDATES SCREENED</div>
        <div style={{ fontSize: '24px', fontWeight: 'bold', color: '#0f172a', marginTop: '0.25rem' }}>{total}</div>
      </div>
      <div style={{ background: '#fff', padding: '1.25rem', borderRadius: '8px', border: '1px solid #e2e8f0' }}>
        <div style={{ fontSize: '12px', color: '#64748b', fontWeight: 'bold' }}>MATCH SCORE BENCHMARK</div>
        <div style={{ fontSize: '24px', fontWeight: 'bold', color: '#0d9488', marginTop: '0.25rem' }}>84.5%</div>
      </div>
      <div style={{ background: '#fff', padding: '1.25rem', borderRadius: '8px', border: '1px solid #e2e8f0' }}>
        <div style={{ fontSize: '12px', color: '#64748b', fontWeight: 'bold' }}>SYSTEM STATUS</div>
        <div style={{ fontSize: '24px', fontWeight: 'bold', color: '#059669', marginTop: '0.25rem' }}>ACTIVE</div>
      </div>
    </div>
  );
}
